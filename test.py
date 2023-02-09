from docx import Document
from getch import pause


FriendName = input("Enter your friend`s name: ")
YourName = input("Enter your name: ")
Date = input("Enter year: ")


replace_FriendName = "#FriendName#"
replace_YourName = "#YourName#"
replace_Date = "#Date#"
file_name = "C:\\Users\\admin\\Desktop\\test\\Sample_Text.docx"


document = Document(file_name)


def find_replace(paragraph_keyword, draft_keyword, paragraph):
    if paragraph_keyword in paragraph.text:
        paragraph.text = paragraph.text.replace(paragraph_keyword, draft_keyword)


for paragraph in document.paragraphs:
    find_replace(replace_FriendName, FriendName, paragraph)
    find_replace(replace_YourName, YourName, paragraph)
    find_replace(replace_Date, Date, paragraph)

document.save("C:\\Users\\admin\\Desktop\\test\\" + FriendName +".docx")


pause('\nDone! Press any key for exit.')