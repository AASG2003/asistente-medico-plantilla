# --- Example -------------------------------------------------------------------
# @extend_schema_view(list=extend_schema(parameters=[QueryExample]))     # documents ?day= in /api/docs/
# class ViewSetExample(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
#     queryset = ModelExample.objects.all()                               # rows to show
#     serializer_class = SerializerExample                                # how they become JSON
#
#     def get_queryset(self):                                             # filter: ?day=2026-11-10
#         query = QueryExample(data=self.request.query_params)
#         query.is_valid(raise_exception=True)                            # 400 if invalid
#         return ModelExample.objects.filter(day=query.validated_data["day"])
#
#     @extend_schema(request=InputExample, responses={201: SerializerExample})
#     @action(detail=True, methods=["post"])                              # POST /examples/{id}/copy/
#     def copy(self, request, pk=None):
#         data = InputExample(data=request.data)
#         data.is_valid(raise_exception=True)
#         try:
#             new = copy_example(self.get_object(), data.validated_data["text"])  # the logic is a service
#         except ValueError as error:
#             return Response({"detail": str(error)}, status=status.HTTP_409_CONFLICT)
#         return Response(SerializerExample(new).data, status=status.HTTP_201_CREATED)
#
#
# class APIViewExample(APIView):                                          # GET /stats/
#     def get(self, request):
#         start = timezone.localdate() - timedelta(days=29)
#         daily = (
#             ModelExample.objects.filter(day__gte=start)                 # date range
#             .values("parent__name", "day")                              # group by parent and day
#             .annotate(total=Sum("price"))                               # one row per group
#         )
#         per_parent = defaultdict(list)                                  # then group in Python
#         for row in daily:
#             per_parent[row["parent__name"]].append(row["total"])
#         rows = [{"parent": name, "days": len(totals)} for name, totals in per_parent.items()]
#         return Response(RowExample(rows, many=True).data)
# -------------------------------------------------------------------------------
