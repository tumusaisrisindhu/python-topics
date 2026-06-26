from history import BrowserHistory

browser = BrowserHistory()

browser.visit("Google")
browser.visit("YouTube")
browser.visit("GitHub")

browser.show_history()

browser.back()
browser.back()

print("\nAfter Back Operations")
browser.show_history()

browser.forward()

print("\nAfter Forward Operation")
browser.show_history()