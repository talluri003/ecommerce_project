from django.db import models

class ProductAnalysis(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)  
    views = models.PositiveIntegerField(default=0)
    purchases = models.PositiveIntegerField(default=0)
    conversion_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    analysis_date = models.DateTimeField(auto_now_add=True)

    def calculate_conversion_rate(self):
        if self.views > 0:
            self.conversion_rate = (self.purchases / self.views) * 100
        else:
            self.conversion_rate = 0
        self.save()

    def __str__(self):
        return f"Analysis for {self.product.name} on {self.analysis_date}"
