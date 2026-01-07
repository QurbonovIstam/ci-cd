class OldPrinter:
    def print_text(self, text):
        return f"Old printer: {text}"




class PrinterAdapter:
    def __init__(self, printer):
        self.printer = printer


    def print(self, text):
        return self.printer.print_text(text)




if __name__ == "__main__":
    old = OldPrinter()
    adapter = PrinterAdapter(old)
    print(adapter.print("Hello"))