from pathlib import Path

from billsplitter.extractor import InstacartExtractor
from billsplitter.splitter import BillSplitter

bill_data = Path("data/receipts/Instacart-03-04-2023.html").read_text()

extractor = InstacartExtractor(bill_data)
delivered_items = extractor.extract_bill()


bill_splitter = BillSplitter(delivered_items, num_people=2, people_names=["Subho", "Aakash"])
bill_splitter.split_bill()
