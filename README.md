# Google Cloud Vision API Text Detection

This Python script utilizes the Google Cloud Vision API to perform text detection on an image. The detected text is then extracted and written to an output text file.

## Prerequisites
1. **Google Cloud Platform Account**: Ensure that you have a Google Cloud Platform account and have set up a project with the Vision API enabled.

2. **Service Account Key**: Obtain a service account key in JSON format from the Google Cloud Console and save it as `ServiceAccountToken.json`. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of this JSON file.

3. **Google Cloud Vision API Client Library**: Install the Google Cloud Vision API client library by running the following command:
   ```bash
   pip install google-cloud-vision
   ```

## Usage

1. Clone or Download:
    - Clone the repository or download the `main.py` file.
2. Place Image:
    - Put the image to analyze in the specified folder (D:\Jaipur Police Hackathon in this example).
    - Adjust the FILE_NAME variable in the script if needed.
3. Update Paths (Optional):
    - Modify FOLDER_PATH and OUTPUT_FILE variables for custom locations.
4. Run Script:
    - Execute the script using `python main.py`.

## Output

* The detected text will be written to the `OUTPUT_FILE` (default: `output.txt`) in the same folder as the script.
* Error messages will be displayed if any issues arise.

## Notes

* Verify the accuracy of folder paths and file names.
* Ensure the service account has necessary permissions.
* Feel free to customize or integrate the script for your specific needs.

## Additional Information

* Google Cloud Vision API Documentation: https://cloud.google.com/vision/docs