# run_tests.py
import unittest
import sys

if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests')  # Ищем тесты в папке tests/
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)

    if result.wasSuccessful():
        print("✅ Все тесты пройдены!")
    else:
        print(f"❌ Не пройдено {result.failures} тестов.")
        sys.exit(1)
