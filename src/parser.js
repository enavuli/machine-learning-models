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
      throw new Error(`Failed to read file: ${error.message}`);
    }
  }

  parseData() {
    if (this.data.length === 0) {
      throw new Error('No data to parse');
    }

    const parsedData = this.data.map(line => {
      const values = line.split(',');
      return values.map(value => parseFloat(value));
    });

    return parsedData;
  }

  async parseFile() {
    await this.readData();
    return this.parseData();
  }
}

module.exports = Parser;