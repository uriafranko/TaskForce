import time

from load_dotenv import load_dotenv

from crews.stock_analysis.crew import StockAnalysisCrew

load_dotenv()


def main():
    start_time = time.time()
    my_financial_crew = StockAnalysisCrew(company="Tesla")

    res = my_financial_crew.run()
    print(res)
    print(f"Time taken: {time.time() - start_time}")
    print("Done!")


if __name__ == "__main__":
    main()
