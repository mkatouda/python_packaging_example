import sys
import corona

country = sys.argv[1] if len(sys.argv) > 1 else ""
print(corona.get(country))
