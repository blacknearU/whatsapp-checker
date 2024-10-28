from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Function to check WhatsApp registration
def check_whatsapp_number(phone_number):
    # Navigate to the WhatsApp Web send message URL
    driver.get(f"https://web.whatsapp.com/send?phone={phone_number}")
    
    # Wait for the page to load and check for the "Send Message" button
    try:
        # Wait for the "Send Message" button to be clickable
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Send Message')]"))
        )
        return f"{phone_number} - Registered on WhatsApp"
    except Exception as e:
        return f"{phone_number} - Not registered on WhatsApp. Error: {str(e)}"

# Main function
def main():
    # Initialize the webdriver for Firefox
    global driver
    driver = webdriver.Firefox()

    # Open the WhatsApp Web interface
    driver.get("https://web.whatsapp.com/")

    # Wait for the user to scan the QR code and log in
    input("Press Enter after scanning the QR code and logging in…")

    # Take input file name from the user
    input_file = input("Please enter the name of the text file containing phone numbers (e.g., phone.txt): ")
    output_file = "whatsapp_check_results.txt"

    results = []

    # Open the file containing the phone numbers
    try:
        with open(input_file, "r") as f:
            for line in f:
                # Strip any whitespace from the line and add +91
                line = line.strip()
                if line:  # Ensure the line is not empty
                    phone_number = f"+91{line}"
                    result = check_whatsapp_number(phone_number)
                    results.append(result)
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        driver.quit()
        return

    # Write results to an output file
    with open(output_file, "w") as out_file:
        for result in results:
            out_file.write(result + "\n")

    print(f"WhatsApp number check completed. Results saved to '{output_file}'.")

    # Close the webdriver
    driver.quit()

if __name__ == "__main__":
    main()
