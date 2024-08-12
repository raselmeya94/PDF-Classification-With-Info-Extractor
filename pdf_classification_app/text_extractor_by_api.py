import re
    
def API_INFO_EXTRACTOR(text):

    print("Extracted Text:: ", text)

    document_type = "OTHER"
    # Determine document type
    if "TIN Certificate" in text or "Taxpayer's Identification Number (TIN) Certificate" in text:
        document_type = "TIN"
    elif "Value Added Tax" in text or "Value Added Tax Registration Certificate" in text or "Customs, Excise and VAT Commissionerate" in text:
        document_type="VAT"
    elif "Certificate of Incorporation" in text or " incorporated\nunder the Companies Act" in text:
        document_type="INCORPORATE"
    elif  "লাইসেন্স" in text or  "ই-ট্রেড লাইসেন্স" in text:
        document_type="TRADE"
    final_details={}

    # TIN KEYS
    TIN_KEYS=[
            "TIN",
            "Name",
            "Registered Address/Permanent Address",
            "Current Address",
            "Previous TIN",
            "Status",
            "Date"
        ]
    
    # VAT KEYS
    VAT_KEYS=[
    'BIN',
    'Name of the Entity',
    'Trading Brand Name',
    'Old BIN',
    'e-TIN',
    'Address',
    'Issue Date',
    'Effective Date',
    'Type of Ownership',
    'Major Area of Economic Activity'
]
    #INCORP KEYS
    Incorp_Keys=[
    'Certificate No.',
    'Company Name',
    'Date of Incorporation',
    'Company Type',
    'Issue Number',
    'Issue Date'
]


    final_details = {"Document Type":document_type}

    # Split the extracted text into lines
    lines = text.strip().split("\n")

    # Process each line to extract key-value pairs
    for line in lines:
        cleaned_line = re.sub(r"\*", "", line).strip()
        
        # Check if the cleaned line contains a key-value pair (indicated by ":")
        if ":" in cleaned_line:
            key, value = cleaned_line.split(":", 1)
            key = key.strip()
            # Remove numbering from the key (if present)
            key = re.sub(r'^\d+\)\s*', '', key)  # Remove leading number and parentheses
            value = value.strip()
            # Add key-value pair to the final_details based on the document type
            if document_type == "TIN" and key in TIN_KEYS:
                final_details.update({key:value})
            elif document_type == "VAT" and key in VAT_KEYS:
                final_details.update({key:value})
            elif document_type == "INCORPORATE" and key in Incorp_Keys:
                final_details.update({key:value})

    return final_details
