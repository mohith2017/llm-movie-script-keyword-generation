import csv
import PyPDF2

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        scene_text = ''

        # Extract text from each page
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            scene_text += page.extract_text()

    return scene_text

# Function to extract scene number and dialogue from scene text
def extract_scene_data(scene_text):
    lines = scene_text.strip().split('\n')
    scene_number = 0
    dialogue = ''

    for line in lines:
        line = line.strip()
        if line.startswith('Scene'):
            scene_number = int(line.split(':')[1].strip())
        elif line:
            dialogue += ' ' + line

    return scene_number, dialogue.strip()

# Extract text from the PDF file
pdf_file_path = '../Data/barbie.pdf'  # Replace with your PDF file path
scene_text_from_pdf = extract_text_from_pdf(pdf_file_path)

# Split the text into scenes using the separator "---"
scenes = scene_text_from_pdf.split('---')

# Write scenes to separate CSV files
for index, scene in enumerate(scenes, start=1):
    scene_number, dialogue = extract_scene_data(scene)

    # Write each scene to a CSV file
    with open(f'scene_{scene_number}.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Scene', 'Dialogue'])
        csv_writer.writerow([scene_number, dialogue])
