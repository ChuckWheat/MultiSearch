import tkinter as tk
import webbrowser


def search_terms():
    # Get the search terms from the text box
    search_terms = text_box.get("1.0", tk.END)

    # Replace commas with newlines to allow for either separator
    search_terms = search_terms.replace(",", "\n")

    # Split the search terms into a list using newlines as the delimiter
    search_terms = search_terms.split("\n")

    # Loop over each search term
    for term in search_terms:
        # Remove any leading or trailing whitespace from the search term
        term = term.strip()

        # Check if the search term is empty and skip it if it is
        if not term:
            continue

        # Create the URL for the Google search
        url = f"https://www.google.com/search?q={term}"

        # Open the URL in a new tab in Chrome
        webbrowser.open(url)


# Create the main window for the GUI
root = tk.Tk()
root.title("Search Terms")

# Create a text box for entering the search terms
text_box = tk.Text(root)
text_box.pack()

# Create a button to submit the search terms
submit_button = tk.Button(root, text="Submit", command=search_terms)
submit_button.pack()

# Start the main loop to run the GUI
root.mainloop()