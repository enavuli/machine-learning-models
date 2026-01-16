package helpers

import (
	"encoding/csv"
	"fmt"
	"log"
	"os"
	"strconv"
)

func LoadCSVData(filename string) ([][]float64, error) {
	file, err := os.Open(filename)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	reader := csv.NewReader(file)
	data, err := reader.ReadAll()
	if err != nil {
		return nil, err
	}

	var floatData [][]float64
	for _, row := range data {
		var floatRow []float64
		for _, value := range row {
			floatValue, err := strconv.ParseFloat(value, 64)
			if err != nil {
				log.Printf("Error parsing value: %s", value)
				return nil, err
			}
			floatRow = append(floatRow, floatValue)
		}
		floatData = append(floatData, floatRow)
	}

	return floatData, nil
}

func SaveCSVData(filename string, data [][]float64) error {
	file, err := os.Create(filename)
	if err != nil {
		return err
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	for _, row := range data {
		var stringRow []string
		for _, value := range row {
			stringRow = append(stringRow, fmt.Sprintf("%f", value))
		}
		if err := writer.Write(stringRow); err != nil {
			return err
		}
	}

	return nil
}