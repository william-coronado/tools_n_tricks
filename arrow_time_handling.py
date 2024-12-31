import arrow
# Create a time object
now = arrow.now()
# Simple date manipulation
future = now.shift(days=3, hours=2)
past = now.shift(weeks=-1)
# Human-readable differences
print(past.humanize())  # outputs: "a week ago"
# Timezone conversion
tokyo_time = now.to('Asia/Tokyo')
paris_time = tokyo_time.to('Europe/Paris')
# Format dates easily
print(f"Here: {now.format('YYYY-MM-DD HH:mm')}")
print(f"Here: {now.humanize()}")
print(f"Future: {future.humanize()}")
print(f"Tokyo: {tokyo_time.format('YYYY-MM-DD HH:mm')}")
print(f"Paris: {paris_time.format('YYYY-MM-DD HH:mm')}")