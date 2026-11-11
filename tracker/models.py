# --- Example -------------------------------------------------------------------
# class ModelExample(models.Model):
#     class Kind(models.TextChoices):                        # choices: value, label
#         FIRST = "first", "First"
#         SECOND = "second", "Second"
#
#     name = models.CharField(max_length=100, unique=True)   # short text, unique
#     notes = models.TextField(blank=True)                   # long text, optional
#     kind = models.CharField(max_length=10, choices=Kind.choices)
#     amount = models.IntegerField(default=0)                # whole number
#     price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
#     active = models.BooleanField(default=True)             # true / false
#     day = models.DateField(default=timezone.localdate)     # date
#     hour = models.TimeField(null=True, blank=True)         # time, optional
#     created_at = models.DateTimeField(auto_now_add=True)   # set when created
#     extra = models.JSONField(null=True, blank=True)        # JSON
#     parent = models.ForeignKey(OtherModel, on_delete=models.CASCADE, related_name="examples")
#
#     class Meta:
#         ordering = ["-day", "name"]                        # default order
#         indexes = [models.Index(fields=["day"])]
#
#     def __str__(self) -> str:                              # how it shows in /admin/
#         return self.name
# -------------------------------------------------------------------------------
