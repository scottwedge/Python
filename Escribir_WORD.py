import win32com.client
 
wordapp = win32com.client.Dispatch("Word.Application") # Create new Word Object
wordapp.Visible = 0 # Word Application should`t be visible
print "Wordapp"
worddoc = wordapp.Documents.Add() # Create new Document Object
worddoc.PageSetup.Orientation = 1 # Make some Setup to the Document:
print "New document"
worddoc.PageSetup.LeftMargin = 20
worddoc.PageSetup.TopMargin = 20
worddoc.PageSetup.BottomMargin = 20
worddoc.PageSetup.RightMargin = 20
print "Margin"
worddoc.Content.Font.Size = 11
print "Font"
worddoc.Content.Paragraphs.TabStops.Add (100)
worddoc.Content.Text = "Hello, I am a text!"
print "Hello, I am a text"
worddoc.Content.MoveEnd
worddoc.Close() # Close the Word Document (a save-Dialog pops up)
wordapp.Quit() # Close the Word Application
"Finished"
raw_input()
