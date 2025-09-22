import datetime
def parsedate_mdy(text: str) -> datetime.datetime:
    return datetime.datetime.strptime(text, "%m/%d/%Y")

def formatdate_ymd(date: datetime.datetime) -> str:
    return date.strftime("%Y-%m-%d")

# Add your test functions here
def test_parsedate_mdy():
    assert parsedate_mdy("12/31/2023") == datetime.datetime(2023, 12, 31)
    assert parsedate_mdy("01/01/2024") == datetime.datetime(2024, 1, 1)

def test_formatdate_ymd():
    assert formatdate_ymd(datetime.datetime(2023, 12, 31)) == "2023-12-31"
    assert formatdate_ymd(datetime.datetime(2024, 1, 1)) == "2024-01-01"