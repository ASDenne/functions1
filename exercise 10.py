def calc_gst(nunber):
    return nunber * 1.15

#main
result = calc_gst(10)
print(result)
result = calc_gst(59.95)
print(f"${result:.2f}")

