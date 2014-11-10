from splinter import Browser

browser = Browser()
browser.visit('http://localhost:8000/')
assert 'Django' in browser.title



