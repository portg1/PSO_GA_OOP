# پروژه شیءگرای مقایسه PSO و GA

این پروژه الگوریتم‌های PSO و GA را برای کمینه‌سازی توابع محک چندبعدی با ساختار شیءگرا پیاده‌سازی می‌کند.

## ساختار پروژه

```text
PSO_GA_OOP/
├── benchmark_functions.py  # توابع هدف
├── optimizer.py             # کلاس پایه و نتیجه اجرا
├── pso.py                   # کلاس PSO
├── ga.py                    # کلاس GA
├── main.py                 # اجرای اصلی
└── README.md               # توضیحات پروژه
```

## اجرا

```bash
cd ~/Desktop/PSO_GA_OOP
python3 main.py
```

## توابع محک

Ackley، Sphere، Rastrigin و Rosenbrock.

## ساختار OOP

`BenchmarkFunctions` توابع هدف را نگهداری می‌کند. `Optimizer` کلاس پایه مشترک الگوریتم‌هاست. کلاس‌های `ParticleSwarmOptimizer` و `GeneticAlgorithm` از آن ارث‌بری می‌کنند. `OptimizationResult` جواب، مقدار تابع و زمان اجرا را نگهداری می‌کند.
