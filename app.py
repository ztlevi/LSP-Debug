import debugpy
debugpy.listen(5678)
debugpy.wait_for_client()

for i in range(100):
    print(i)

print()