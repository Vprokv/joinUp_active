from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "John"}]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id": 3, "name": "axaxa"}, status=status.HTTP_201_CREATED)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_program": 1,
                "program_name": "Адаптация HR специалиста",
                "description": "Программа адаптации предназначена для новых специалистов",
                "duration_day": 16,
                "tier": 12,
                "id_customer": 2,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2
            },
            {
                "id_program": 2,
                "program_name": "Адаптация менеджера по продажам",
                "description": "Программа адаптации предназначена для новых специалистов",
                "duration_day": 21,
                "tier": 12,
                "id_customer": 2,
                "status": 4,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2
            },

        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id_program": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationLevelTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_level": 1,
                "level_name": "Общие сведения",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_program": [1, 2]
            },
            {
                "id_level": 2,
                "level_name": "Должностные инструкции",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 4,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 12,
                "id_program": [3, 7]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id_level": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationStageTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_stage": 1,
                "stage_name": "Общие сведения",
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "point": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [3, 4]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id_stage": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationBlockTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_block": 1,
                "block_name": "Общие сведения",
                "description": "это описание блока программ",
                "tier": 12,
                "id_stage": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2
            },
            {
                "id_block": 3,
                "block_name": "Общие тоже сведения",
                "description": "это  тоже описание блока программ",
                "tier": 12,
                "id_stage": 34,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id_block": 2}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationGoalTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_goal": 1,
                "description": "Повышение мотивации",
                "tier": 12,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_program": [1, 2]
            },
            {
                "id_goal": 2,
                "description": "увеличение продаж",
                "tier": 12,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_program": [3, 4]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id_goal": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationDocumentTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_document": 1,
                "document_name": "Личное дело",
                "document_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_program": [1, 2]
            },
            {
                "id_document": 2,
                "document_name": "должностные инструкции",
                "document_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 2,
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_program": [3, 4]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id_document": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdaptationContactTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_contact": 1,
                "id_program": 2,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "post": "менеджер по продажам",
                "role": "какая-то роль",
                "status": 2,
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [1, 2]
            },
            {
                "id_contact": 2,
                "id_program": 3,
                "last_name": "Андреев",
                "first_name": "Андрей",
                "middle_name": "Андреевич",
                "post": "начальник отдела рекламы",
                "role": "какая-то роль",
                "status": 2,
                "illustration_link": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "create_date": "Sun, 31 Dec 1899 00:00:00 GMT",
                "create_user": 2,
                "id_level": [4, 5]
            }
        ]
        return Response(data)

    def post(self, request, *args, **kwargs):
        return Response({"id_contact": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_204_NO_CONTENT)


class LnkLevelProgramTestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({"id_lnk_level_program": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)


class LnkStageLevelTestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({"id_lnk_level_program": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)


class LnkGoalProgramTestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({"id_lnk_goal_program": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)


class LnkDocumentProgramTestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({"id_lnk_document_program": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)


class LnkContactProgramTestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({"id_lnk_contact_program": 3}, status=status.HTTP_200_OK)

    # def put(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_200_OK)


# class CustomerTestAPIView(APIView):


# Нет данных


# class LicensePackTestAPIView(APIView):


# Нет данных


# class UserServiceUserTestAPIView(APIView):


# Нет данных


class UserServiceSMSTestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)


class UserServiceTokenTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({"2336D7B2F8EFDC58B3EE3F5CD99BB"})


# class UserServiceCandidateTestAPIView(APIView):


# Нет данных


# class EmployeeTestAPIView(APIView):


# Нет данных


class IEmployeeServiceAuthenticationTestAPIView(APIView):

    def post(self, request, *args, **kwargs):
        return Response({"OK"}, status=status.HTTP_200_OK)


class RequestUserToken(APIView):

    def get(self, request, *args, **kwargs):
        return Response("2336D7B2F8EFDC58B3EE3F5CD99BB")


class IAdaptationProgramTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        return Response({"id_program": 3}, status=status.HTTP_200_OK)


class ILevelStagesTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_level": 1,
                "level_name": "Общие сведения",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 2,
                "stages": [
                    {
                        "id_stage": 1,
                        "stage_name": "stage 1",
                        "illustration_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                        "tier": 12,
                        "point": 122,
                        "is_completed": "true"
                    },
                    {
                        "id_stage": 2,
                        "stage_name": "stage 2",
                        "illustration_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                        "tier": 12,
                        "point": 122,
                        "is_completed": "true"
                    },
                    {
                        "id_stage": 3,
                        "stage_name": "stage 3",
                        "illustration_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                        "tier": 12,
                        "point": 122,
                        "is_completed": "true"
                    }
                ]
            },
            {
                "id_level": 2,
                "level_name": "Общие сведения 2",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
                "tier": 12,
                "status": 2,
                "stages": [
                    {
                        "id_stage": 1,
                        "stage_name": "stage 1",
                        "illustration_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                        "tier": 12,
                        "point": 122,
                        "is_completed": "true"
                    },
                    {
                        "id_stage": 2,
                        "stage_name": "stage 2",
                        "illustration_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                        "tier": 12,
                        "point": 122,
                        "is_completed": "true"
                    },
                    {
                        "id_stage": 3,
                        "stage_name": "stage 3",
                        "illustration_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                        "tier": 12,
                        "point": 122,
                        "is_completed": "true"
                    }
                ]
            },
        ]
        return Response(data)


class IGoalsTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_goal": 1,
                "goal_name": "Цель 1",
                "description": "Цель 1",
                "tier": 12,
                "is_completed": "true"
            },
            {
                "id_goal": 2,
                "goal_name": "Цель 2",
                "description": "Цель 2",
                "tier": 12,
                "is_completed": "true"
            },
        ]
        return Response(data)


class IDocumentsTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_document": 1,
                "document_name": "document 1",
                "document_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                "tier": 12,
            },
            {
                "id_document": 2,
                "document_name": "document 2",
                "document_link": "https://upload.wikimedia.org/wikipedia/commons/d/df/Open_sea_%28july_2021%29.jpg",
                "tier": 12,
            },
        ]
        return Response(data)


class IContactsTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_contact": 1,
                "last_name": "Иванов",
                "first_name": "Иван",
                "middle_name": "Иванович",
                "post": "менеджер по продажам",
                "role": "какая-то роль",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
            },
            {
                "id_contact": 2,
                "last_name": "Андреев",
                "first_name": "Андрей",
                "middle_name": "Андреевич",
                "post": "начальник отдела рекламы",
                "role": "какая-то роль",
                "illustration": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fru.depositphotos.com%2Fstock-photos%2F%25D1%2580%25D0%25B0%25D0%25B1%25D0%25BE%25D1%2582%25D0%25B0-%25D0%25B2-%25D0%25B8%25D0%25BD%25D1%2582%25D0%25B5%25D1%2580%25D0%25BD%25D0%25B5%25D1%2582%25D0%25B5.html&psig=AOvVaw0MVUI_amjMnc32xcy1SKU2&ust=1638170544123000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCPi34PzCuvQCFQAAAAAdAAAAABAD",
            }
        ]
        return Response(data)


class IBlocksTestAPIView(APIView):

    def get(self, request, *args, **kwargs):
        data = [
            {
                "id_block": 1,
                "block_name": "block 1",
                "description": "description block 1",
                "tier": 12,
            },
            {
                "id_block": 2,
                "block_name": "block 2",
                "description": "description block 3",
                "tier": 15,
            }
        ]
        return Response(data)
