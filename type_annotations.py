class Book:
    def __init__(self, author: str, title: str, pages: int) -> None:
        self.author = author
        self.title = title
        self.pages = pages

    def __len__(self) -> int:
        return self.pages


def calculate_average(numbers: list[int]) -> float:
    total = sum(numbers)
    return total / len(numbers)


def calculate_total_sales(sales: dict[str, int]) -> int:
    return sum(sales.values())


if __name__ == "__main__":
    print(len(Book("George R. R. Martin", "A Game of Thrones", 694)))

    data: list[int] = [1, 2, 3, 4, 5]
    average: float = calculate_average(data)
    print("The average is:", average)

    sales_data: dict[str, int] = {"product_a": 100, "product_b": 250, "product_c": 80, "product_d": 150}
    print("Sales data for product C:", sales_data["product_c"])
    total_sales: int = calculate_total_sales(sales_data)
    print("Total sales:", total_sales)
