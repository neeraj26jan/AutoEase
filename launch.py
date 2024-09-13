from autoease import AutoEase
import time
import webbrowser

# Open the web browser
webbrowser.open('https://www.google.com')

# Wait for the browser to open
time.sleep(3)

autoease = AutoEase()

# Find search box and type "Hello World!"
elements = autoease.find_elements('search.jpg', min_confidence=0.8)
autoease.type_at(elements[0], 'Hello World!')

# Find Google Search button and click it
elements = autoease.find_elements('google_search.jpg', min_confidence=0.8)
autoease.click_at(elements[0])