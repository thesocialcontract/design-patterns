import range_context as r
import normal_state as n

context = r.RangeContext()
context.set_state(n.NormalState(context, 0, -10, 10))

context.add(5)      # Normal:   5
context.sub(5)      # Normal:   0
context.add(10)     # Surplus:  10
context.add(10)     # Surplus:  20
context.add(10)     # Surplus:  20
context.sub(20)     # Normal:   0
context.sub(5)      # Normal:  -5
context.add(5)      # Normal:   0
context.sub(10)     # Deficit: -10
context.sub(10)     # Deficit: -10
context.sub(10)     # Deficit: -20
context.sub(10)     # Deficit: -20
context.add(25)     # Surplus:  15
context.sub(30)     # Deficit: -15
