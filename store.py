from transaction import Transaction 

class Exporter:
    def export(self, transactions):
        raise NotImplementedError("Subclasses must implement the export method")

class CsvExporter(Exporter):
    def export(self, transactions, filename="report.csv"):
        try:
            with open(filename, "w") as file:
                file.write("amount,category,description,t_type\n")
                for transaction in transactions:
                    file.write(f"{transaction.amount},{transaction.category},{transaction.description},{transaction.t_type}\n")

        except Exception as e:
            print(f"An error occurred while exporting to CSV: {e}")

        else:
            print(f"Transactions successfully exported to {filename}")

        finally:
            print("Export process completed.")

def save__to_file(transactions, filename="report.txt"):
    try:
        with open(filename, "w") as file:
            for transaction in transactions:
                file.write(f"{transaction.amount},{transaction.category},{transaction.description},{transaction.t_type}\n")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")
    else:
        print(f"Transactions successfully saved to {filename}")
    finally:
        print("Save process completed.")

def load_file(filename="report.txt"):
    transactions = []
    try:
        with open(filename, "r") as file:
            for line in file:
                amount, category, description, t_type = line.strip().split(",")
                transaction = Transaction(float(amount), category, description, t_type)
                transactions.append(transaction)
    except Exception as e:
        print(f"An error occurred while loading from file: {e}")
    else:
        print(f"Transactions successfully loaded from {filename}")
    finally:
        print("Load process completed.")
    return transactions


