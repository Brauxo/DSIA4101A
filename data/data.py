from data.cleaning import cleaning

def data_process(url):
    # Extraction and cleaning of the data
    data = cleaning(url)

    data.load_data()  # Load the data
    data.clean_data()  # Clean the data using the Extract class
    cleaned_data = data.filtered_data()  # Get the organized data

    return cleaned_data
