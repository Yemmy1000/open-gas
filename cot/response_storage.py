class ResponseStorage:
    def __init__(self):
        """Initialize an empty dictionary to store responses."""
        self.storage = {}

    def add_mapping(self, response, component):
        """
        Add a mapping of component to response.

        Parameters:
        response (str): The response text to store.
        component (str): The component associated with the response.
        """
        self.storage[component] = response

    def get_all_mappings(self):
        """
        Retrieve all stored mappings.

        Returns:
        dict: The dictionary of all stored mappings.
        """
        return self.storage

    def get_mapping(self, component):
        """
        Retrieve the response associated with a specific component.

        Parameters:
        component (str): The component to look up.

        Returns:
        str: The response associated with the component, or None if the component is not found.
        """
        return self.storage.get(component)

# Example usage
def main():
    response_storage = ResponseStorage()

    # Adding some mappings
    response_storage.add_mapping("This is the first response", "first")
    response_storage.add_mapping("This is the second response", "second")
    response_storage.add_mapping("This is the third response", "third")

    # Retrieving and printing all mappings
    all_mappings = response_storage.get_all_mappings()
    print("All stored mappings:", all_mappings)

    # Retrieving and printing a specific mapping
    specific_mapping = response_storage.get_mapping("second")
    print("Response for component 'second':", specific_mapping)

if __name__ == "__main__":
    main()
