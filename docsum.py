def split_document_into_chunks(text):
    r'''
    Split the input text into smaller chunks so that an LLM can process chunks individually.

    >>> split_document_into_chunks('This is a sentence. \n\n This is another paragraph')
    ['This is a sentence.', 'This is another paragraph.']
    
    >>> split_document_into_chunks('')
    []
    
    >>> split_document_into_chunks('\n\n\n\n')
    []
    
    >>> split_document_into_chunks('This is a single paragraph.')
    ['This is a single paragraph.']
    
    >>> split_document_into_chunks('Paragraph one.\n\n\n\nParagraph two.\n\nParagraph three.')
    ['Paragraph one.', 'Paragraph two.', 'Paragraph three.']
    
    >>> split_document_into_chunks('   Paragraph one. \n\n  Paragraph two.  \n\n  Paragraph three.   ')
    ['Paragraph one.', 'Paragraph two.', 'Paragraph three.']
    
    >>> split_document_into_chunks('Line one.\n\nLine two.\n\nLine three.')
    ['Line one.', 'Line two.', 'Line three.']
    
    >>> split_document_into_chunks('Para one.\n\nPara two.\n\nPara three.\n\nPara four.\n\nPara five.')
    ['Para one.', 'Para two.', 'Para three.', 'Para four.', 'Para five.']
    
    '''
    return text.split('\n\n')

import os
from groq import Groq
import argparse

#parse command line args 
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# line 7+8 = args.filename will contain the first string after program name on command line

client = Groq(
    # This is the default and can be omitted
    api_key=os.environ.get('GROQ_API_KEY'),
)

with open(args.filename) as f: 
    text=f.read()

    '''
    We need to call the split_document_into_chunks on text. 
    Then for reach paragraph in the output list, call the LLM code below to summarize it. Put the summary into a new list. 
    Concatenate that new list into one smaller document. 
    recall the LLM code below on the new smaller document. 
    '''

chat_completion = client.chat.completions.create(
    messages=[
        { 
            'role': 'system',
            'content': 'Summarize the input text below in less than 100 words and use a 1st grade reading level.',
        },
        {
            "role": "user",
            "content": text,
        }
    ],
    model="llama3-8b-8192",
)
print(chat_completion.choices[0].message.content)
#
