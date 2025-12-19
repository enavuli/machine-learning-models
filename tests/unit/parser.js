const fs = require('fs');
const path = require('path');

class Parser {
  constructor(filePath) {
    this.filePath = filePath;
    this.data = [];
  }

  async readData() {
    try {
      const content = await fs.promises.readFile(this.filePath, 'utf8');
      this.data = content.split('\n').map(line => line.trim());
    } catch (error) {
      console.error(`Error reading file: ${error.message}`);
    }
  }

  parseData() {
    const parsedData = this.data.map(line => {
      const values = line.split(',');
      return {
        feature1: parseFloat(values[0]),
        feature2: parseFloat(values[1]),
        label: parseInt(values[2])
      };
    });
    return parsedData;
  }

  saveParsedData(outputFilePath) {
    const parsedData = this.parseData();
    const output = JSON.stringify(parsedData, null, 2);
    fs.writeFile(outputFilePath, output, 'utf8', error => {
      if (error) {
        console.error(`Error writing file: ${error.message}`);
      }
    });
  }
}

module.exports = Parser;