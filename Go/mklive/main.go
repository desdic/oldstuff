package main

/*
	Parse mklive from nagios/icinga/shinken
*/

import (
	"bufio"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log"
	"net"
	"strconv"
	"strings"
	"time"
)

type MKResponse struct {
	status   int
	recieved int
	data     []MKRow
}

type MKRow map[string]interface{}

func (r MKRow) GetKey(key string) (interface{}, error) {
	if k, ok := r[key]; ok {
		return k, nil
	}
	return nil, errors.New("Key does not exist")
}

func (r MKRow) String(key string) (string, error) {
	k, err := r.GetKey(key)
	if err != nil {
		return "", err
	}

	str, ok := k.(string)
	if !ok {
		return "", errors.New(key + " is not a string")
	}

	return str, nil
}

func (r MKRow) Int(key string) (int64, error) {
	k, err := r.GetKey(key)
	if err != nil {
		return 0, err
	}

	i, ok := k.(int64)
	if !ok {
		return 0, errors.New(key + " is not a int64")
	}

	return int64(i), nil
}

func (r MKRow) Float(key string) (float64, error) {
	k, err := r.GetKey(key)
	if err != nil {
		return 0, err
	}

	i, ok := k.(float64)
	if !ok {
		return 0, errors.New(key + " is not a float64")
	}

	return float64(i), nil
}

func (r MKRow) Time(key string) (time.Time, error) {
	k, err := r.GetKey(key)
	if err != nil {
		return time.Time{}, err
	}

	i, ok := k.(int64)
	if !ok {
		return time.Time{}, errors.New(key + " is not a time")
	}

	return time.Unix(int64(i), 0), nil
}

type MKQuery struct {
	table   string
	columns []string
}

func (q *MKQuery) Build() string {
	// Build query
	query := "GET " + q.table
	if len(q.columns) > 0 {
		query += "\nColumns: " + strings.Join(q.columns, " ")
	}
	query += "\nResponseHeader: fixed16"
	query += "\nOutputFormat: json"
	query += "\n\n"
	return query
}

func (q *MKQuery) Query(host string, port string) (MKResponse, error) {

	var r MKResponse

	r.status = 500
	r.recieved = 0

	hoststring := host + ":" + port
	conn, err := net.Dial("tcp", hoststring)
	if err != nil {
		log.Printf("Connect failed to %s", hoststring)
		return r, err
	}

	defer conn.Close()

	fmt.Fprintf(conn, q.Build())
	mkconn := bufio.NewReader(conn)

	header, err := mkconn.ReadString('\n')
	if err != nil {
		log.Println("Unable to read header")
		return r, err
	}

	status, err := strconv.Atoi(header[:3])
	if err != nil {
		log.Println("Unable to convert return code to integer")
		return r, err
	}

	resp, err := strconv.Atoi(strings.TrimSpace(header[4:15]))
	if err != nil {
		log.Println("Unable to convert return code to integer")
		return r, err
	}

	var mkoutput [][]interface{}
	jdec := json.NewDecoder(mkconn)
	for {
		err := jdec.Decode(&mkoutput)
		if err == io.EOF {
			break
		} else if err != nil {
			log.Println("Unable to parse json")
			return r, err
		}
	}

	r.data = make([]MKRow, len(mkoutput[0:]))

	for num, row := range mkoutput[0:] {
		tmp := make(MKRow)
		for key, value := range row {
			tmp[q.columns[key]] = value
		}
		r.data[num] = tmp
	}

	r.status = status
	r.recieved = resp

	return r, nil
}

func main() {

	var q MKQuery

	q = MKQuery{table: "hosts", columns: []string{"host_name", "last_check"}}

	res, err := q.Query("icinga1.example.com", "6558")
	if err != nil {
		log.Printf("Failed to get response: %s", err)
	}
	log.Printf("%#v", res)

}
