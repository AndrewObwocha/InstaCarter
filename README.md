# InstaCarter: Automate Your Instacart Shopping Lists

## Smart shopping list creation without the clicking.

InstaCarter is a Python CLI application that automates shopping list creation on Instacart. The application features a command-line interface for user input, backend integration with Instacart's API endpoints, and local product ID mapping stored in Python dictionaries. It validates user input and generates structured JSON payloads for seamless Instacart integration with optional expiration settings.

- **Automated Shopping List Creation** - Build Instacart shopping lists programmatically without manual entry.
- **Intelligent Product Mapping** - Automatically maps product names to Instacart product IDs for faster processing.
- **Simple CLI Interface** - Intuitive command-line prompts guide users through the shopping list creation process.

## Installation and Usage

### For Regular Users

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AndrewObwocha/InstaCarter.git
   cd InstaCarter
   ```

2. **Install Python (if not already installed):**
   Download Python 3.8+ from [python.org](https://www.python.org)

3. **Run the application:**

   ```bash
   python main.py
   ```

4. **Follow the prompts:**
   - Enter the number of items you want to add
   - For each item, provide the product name, quantity, and unit of measurement
   - The application will send your list to Instacart

> **Note:** Before running, ensure your Instacart API key is set in `utils.py` (replace `<API-key>` in the headers).

## For Developers

### Project Structure

- `main.py` - Entry point with CLI input handling
- `models.py` - `LineItem` class for shopping item representation
- `services.py` - API communication and payload construction
- `utils.py` - Product ID mappings, headers, and payload templates

### Setup

1. Clone the repository and navigate to the directory
2. Ensure Python 3.8+ is installed
3. Review and update the Instacart API key in `utils.py`
4. Run with `python main.py`

### Key Components

**LineItem Model:** Represents a shopping item with name, quantity, unit, and automatically resolved product ID from the local mapping.

**API Service:** Handles the Instacart API communication, converting line items into properly formatted requests.

**Product Mapping:** Local dictionary (`id_mapping` in `utils.py`) maps product names to Instacart product IDs for quick resolution.

## Contributing

We welcome contributions! Here's how you can help:

1. **Report Issues** - Found a bug? Use the Issues tab to report it with details about the behavior and environment.
2. **Submit Enhancements** - Have a feature idea? Open an issue describing the enhancement and discuss the approach.
3. **Submit Pull Requests** - For bug fixes or features:
   - Create a new branch from `main`
   - Make your changes with clear commit messages
   - Submit a PR referencing any related issues
   - Ensure code follows the existing style

### Areas for Contribution

- Expand the product ID mapping database
- Add support for additional grocery services
- Improve error handling and user feedback
- Add unit tests for better code reliability
- Enhance the CLI with interactive features

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
