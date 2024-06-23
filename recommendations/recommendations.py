# recommendations/recommendations.py

from concurrent import futures
import random
import grpc

from recommendations_pb2 import (
    BookCategory,
    BookRecommendation,
    RecommendationResponse,
)

import recommendations_pb2_grpc

books_by_category = {
    BookCategory.MYSTERY: [
        BookRecommendation(id=1, title="Мальтийский сокол"),
        BookRecommendation(id=2, title="Убийство в Восточном экспрессе"),
        BookRecommendation(id=3, title="Собака Баскервилей"),
        BookRecommendation(id=4, title="Автостопом по галактике"),
        BookRecommendation(id=5, title="Игра Эндера"),
        BookRecommendation(id=6, title="Тень Пумы"),
        BookRecommendation(id=7, title="Загадка Сэмюэля Фуллера"),
        BookRecommendation(id=8, title="Последний из Могикан"),
        BookRecommendation(id=9, title="Белый заяц"),
        BookRecommendation(id=10, title="Корабль дураков"),
    ],
    BookCategory.SCIENCE_FICTION: [
        BookRecommendation(id=11, title="Дюна"),
        BookRecommendation(id=12, title="1984"),
        BookRecommendation(id=13, title="Властелин колец"),
        BookRecommendation(id=14, title="Атлантида"),
        BookRecommendation(id=15, title="Сто лет тому вперед"),
        BookRecommendation(id=16, title="Антивирус"),
        BookRecommendation(id=17, title="Обитаемый остров"),
        BookRecommendation(id=18, title="Пепельный город"),
        BookRecommendation(id=19, title="Речи в космосе"),
        BookRecommendation(id=20, title="Сталкер"),
    ],
    BookCategory.SELF_HELP: [
        BookRecommendation(id=21, title="Семь навыков высокоэффективных людей"),
        BookRecommendation(id=22, title="Как завоёвывать друзей и оказывать влияние на людей"),
        BookRecommendation(id=23, title="Человек в поисках смысла"),
        BookRecommendation(id=24, title="Принцип 80/20"),
        BookRecommendation(id=25, title="Сила подсознания"),
        BookRecommendation(id=26, title="Как остановить время"),
        BookRecommendation(id=27, title="Секреты успеха"),
        BookRecommendation(id=28, title="Отказ от гнева"),
        BookRecommendation(id=29, title="Фокус на позитиве"),
        BookRecommendation(id=30, title="Счастье: как найти его и сохранить"),
    ],
}

class RecommendationService(recommendations_pb2_grpc.RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in books_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found")

        books_for_category = books_by_category[request.category]
        num_results = min(request.max_results, len(books_for_category))
        books_to_recommend = random.sample(books_for_category, num_results)

        return RecommendationResponse(recommendations=books_to_recommend)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    recommendations_pb2_grpc.add_RecommendationsServicer_to_server(
        RecommendationService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()