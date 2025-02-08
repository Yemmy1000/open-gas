class ResponseExtractor:
    def __init__(self):
        pass

    def extract_values(self, response, keywords):
        """
        Extract values from the response that are present in the keywords list.

        Parameters:
        response (str): The text to search within.
        keywords (list): The list of keywords to search for.

        Returns:
        list: A list of keywords found in the response.
        """
        found_keywords = [keyword for keyword in keywords if keyword in response]
        return found_keywords

# Example usage
def main():
    response_text = "This is a sample response containing cybersecurity and certain keywords like AI, cybersecurity, and machine learning."
    keywords_list = ["AI", "cybersecurity", "blockchain", "machine learning"]

    extractor = ResponseExtractor()
    found_values = extractor.extract_values(response_text, keywords_list)
    
    print("Keywords found in the response:", found_values)

if __name__ == "__main__":
    main()
