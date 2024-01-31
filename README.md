# Basic Monero Price Tracker

This very simple Flask application provides real-time Monero (XMR) cryptocurrency price information in Euros (EUR). It utilizes the CryptoCompare API to fetch the latest price data and displays it on a web page.

## Features

- **Current Price Display:** The main page shows the current price of Monero in Euros.
- **Manual Refresh:** Users can manually refresh the price information by visiting the '/refresh' route.
- **Error Handling:** Custom error page for 404 errors.

## Code Overview

The application is built with Flask and utilizes the `requests` library for API requests.

### Web Routes

- **Main Page (`/`):** Displays the current price of Monero in Euros.
- **Refresh (`/refresh`):** Manually triggers a refresh to update the price information.

### External API Integration

- The [CryptoCompare API](https://min-api.cryptocompare.com/) is used to fetch the current price of Monero in Euros.

### Error Handling

- Custom error page for 404 errors.

### Running the Application

1. Install the required dependencies `pip install Flask`, `pip install requests`.
2. Run the application (in debug mode only) `python app.py`.
3. Access the application at `http://127.0.0.1:5000/` in your web browser.
4. The main page displays the current price of Monero in Euros.

## Disclaimer

This project is for educational purposes only. Any actions and or activities related to the material contained within this project is solely your responsibility. I assume no liability and are not responsible for any misuse or damage caused by this program.

## Contact

Created by [Insomnia](https://github.com/currentlyonciawatchlist/) - feel free to contact me!
