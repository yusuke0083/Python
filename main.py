test_name = "TEST001"
expected_value = 25.5
actual_value = 25.0

print(test_name)

if expected_value == actual_value:
    print("Pass")
    print(f"期待値：{expected_value}と実際値：{actual_value}は一致しました。")
else:
    print("Fail")
    print(f"期待値：{expected_value}と実際値：{actual_value}は一致しませんでした。")