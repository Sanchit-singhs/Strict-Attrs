import dataclasses
import timeit
from typing import List, Optional, Union

import pydantic
from attrs import asdict, define, field, validators
from pydantic import ConfigDict

from dataclass_test import *

# @strict_dataclass
# class MeetingStartedDataClass:
#     attributes: int
#     meeting_start_time: str
#     a: int
#     b: str


# @strict_dataclass
# class MeetTestDataClass:
#     meet_data_list: List[MeetingStartedDataClass]
#     asd: str


# @define
# class MeetingStartedData:
#     attributes: int = field(validator=validators.instance_of(int))
#     meeting_start_time: str = field(validator=validators.instance_of(str))
#     a: int = field(validator=validators.instance_of(int))
#     b: str = field(validator=validators.instance_of(str))


# @define
# class MeetTest:
#     meet_data_list: List[MeetingStartedData] = field(
#         validator=validators.deep_iterable(
#             member_validator=validators.instance_of(MeetingStartedData),
#             iterable_validator=validators.instance_of(list),
#         )
#     )
#     asd: str = field(validator=validators.instance_of(str))


# def make_attr_obj():
#     MeetTest(
#         [
#             MeetingStartedData(1, "2", 3, "awsd"),
#             MeetingStartedData(1, "2", 3, "awsddas"),
#             MeetingStartedData(1, "2", 3, "awscsdsad"),
#         ],
#         "32",
#     )


# def make_dataclass_obj():
#     MeetTestDataClass(
#         [
#             MeetingStartedDataClass(1, "2", 3, "awsd"),
#             MeetingStartedDataClass(1, "2", 3, "ds"),
#             MeetingStartedDataClass(1, "2", 3, "awssadaad"),
#         ],
#         "32",
#     )


# attr_obj = MeetTest(
#     [
#         MeetingStartedData(1, "2", 3, "awsd"),
#         MeetingStartedData(1, "2", 3, "awsddas"),
#         MeetingStartedData(1, "2", 3, "awscsdsad"),
#     ],
#     "32",
# )

# dataclass_obj = MeetTestDataClass(
#     [
#         MeetingStartedDataClass(1, "2", 3, "awsd"),
#         MeetingStartedDataClass(1, "2", 3, "ds"),
#         MeetingStartedDataClass(1, "2", 3, "awssadaad"),
#     ],
#     "32",
# )


# def create_attr_dict():
#     asdict(attr_obj)


# def create_dataclass_dict():
#     dataclasses.asdict(dataclass_obj)


# time_1 = timeit.timeit(make_attr_obj, number=100000)
# time_2 = timeit.timeit(create_attr_dict, number=100000)
# time_3 = timeit.timeit(make_dataclass_obj, number=100000)
# time_4 = timeit.timeit(create_dataclass_dict, number=100000)

# print(f"Time taken to create attr objects is : {time_1}")
# print(f"Time taken to create dict of attr object is : {time_2}")
# print(f"Time taken to create dataclass objects is : {time_3}")
# print(f"Time taken to create dict of dataclass object is : {time_4}")

""" ------- ---------- -------- ------ ---------- -------- ---------- ---------- ------ ------ """


# @strict_dataclass
# class TestDAta:
#     a: int
#     b: str


# @define
# class MeetingStartedData:
#     attributes: Union[int, str] = field(
#         validator=validators.instance_of((int, str))
#     )
#     meeting_start_time: str = field(validator=validators.instance_of(str))
#     a: int = field(validator=validators.instance_of(int))
#     c: List[Union[str, TestDAta]] = field(
#         validator=validators.deep_iterable(
#             member_validator=validators.instance_of((str, TestDAta)),
#             iterable_validator=validators.instance_of(list),
#         )
#     )
#     b: Optional[str] = field(
#         default=None, validator=validators.optional(validators.instance_of(str))
#     )


# @strict_dataclass
# class MeetingStartedDataClass:
#     attributes: Union[int, str]
#     meeting_start_time: str
#     a: int
#     c: List[Union[str, TestDAta]]
#     b: Optional[str]


# @define
# class MeetTest:
#     meet_data_list: List[MeetingStartedData] = field(
#         validator=validators.deep_iterable(
#             member_validator=validators.instance_of(MeetingStartedData),
#             iterable_validator=validators.instance_of(list),
#         )
#     )
#     asd: str = field(validator=validators.instance_of(str))


# @strict_dataclass
# class MeetTestDataClass:
#     meet_data_list: List[MeetingStartedDataClass]
#     asd: str


# def make_attr_obj():
#     MeetTest(
#         [
#             MeetingStartedData(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#             MeetingStartedData(
#                 "1", "2", 3, ["1", "2", TestDAta(11, "2")], "sdfsddas"
#             ),
#             MeetingStartedData(
#                 "1", "2", 3, ["1", "2", TestDAta(14, "2")], "sfsddas"
#             ),
#         ],
#         "32",
#     )


# def make_dataclass_obj():
#     MeetTestDataClass(
#         [
#             MeetingStartedDataClass(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#             MeetingStartedDataClass(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#             MeetingStartedDataClass(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#         ],
#         "32",
#     )


# attr_obj = MeetTest(
#     [
#         MeetingStartedData(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#         MeetingStartedData(
#             "1", "2", 3, ["1", "2", TestDAta(11, "2")], "sdfsddas"
#         ),
#         MeetingStartedData(
#             "1", "2", 3, ["1", "2", TestDAta(14, "2")], "sfsddas"
#         ),
#     ],
#     "32",
# )

# dataclass_obj = MeetTestDataClass(
#     [
#         MeetingStartedDataClass(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#         MeetingStartedDataClass(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#         MeetingStartedDataClass(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#     ],
#     "32",
# )


# def create_attr_dict():
#     asdict(attr_obj)


# def create_dataclass_dict():
#     dataclasses.asdict(dataclass_obj)


# time_1 = timeit.timeit(make_attr_obj, number=100000)
# time_2 = timeit.timeit(create_attr_dict, number=100000)
# time_3 = timeit.timeit(make_dataclass_obj, number=100000)
# time_4 = timeit.timeit(create_dataclass_dict, number=100000)


# print(f"Time taken to create attr objects is : {time_1}")
# print(f"Time taken to create dict of attr object is : {time_2}")
# print(f"Time taken to create dataclass objects is : {time_3}")
# print(f"Time taken to create dict of dataclass object is : {time_4}")

""" === ============  === = == = == == == == == == == == = == == == = == = == = = == == = == = = == """


# @strict_dataclass
# class MeetingStartedDataClass:
#     attributes: int
#     meeting_start_time: str
#     a: int
#     b: str


# @strict_attrs
# class MeetingStartedAttr:
#     attributes: int
#     meeting_start_time: str
#     a: int
#     b: str


# dataclass_obj = MeetingStartedDataClass(1, "2", 3, "4")
# attr_obj = MeetingStartedAttr(1, "2", 3, "4")


# @strict_attrs
# class MeetTestAttr:
#     meet_data_list: List[MeetingStartedAttr]
#     asd: str


# @strict_dataclass
# class MeetTestDataClass:
#     meet_data_list: List[MeetingStartedDataClass]
#     asd: str


# new_obj_attr = MeetTestAttr([MeetingStartedAttr(1, "2", 3, "4")], "2")
# new_obj_dataclass = MeetTestDataClass(
#     [MeetingStartedDataClass(1, "2", 3, "4")], "3"
# )


# def test_attr():
#     MeetTestAttr([MeetingStartedAttr(1, "2", 3, "4")], "2")


# def test_database():
#     MeetTestDataClass([MeetingStartedDataClass(1, "2", 3, "4")], "3")


# def test_attr_dict():
#     attrs.asdict(new_obj_attr)


# @timeit.timeit()
# def test_dataclass_dict():
#     dataclasses.asdict(new_obj_dataclass)


# time_1 = timeit.timeit(test_attr, number=100000)
# time_2 = timeit.timeit(test_database, number=100000)
# time_3 = timeit.timeit(test_attr_dict, number=100000)
# time_4 = timeit.timeit(test_dataclass_dict, number=100000)


# print(f"Time taken to create attr objects is : {time_1}")
# print(f"Time taken to create dataclass objects is : {time_2}")
# print(f"Time taken to create attrs dict is : {time_3}")
# print(f"Time taken to create dataclass dict is : {time_4}")

""" --------------- --------------- -- - -- - -- -- -- -- - - - -- - - -- - - -- - """


# @strict_dataclass
# class TestDAta:
#     a: int
#     b: str


# @strict_attrs
# class MeetingStartedData:
#     attributes: Union[int, str]
#     meeting_start_time: str
#     a: int
#     c: List[Union[str, TestDAta]]
#     b: Optional[str]


# @strict_dataclass
# class MeetingStartedDataClass:
#     attributes: Union[int, str]
#     meeting_start_time: str
#     a: int
#     c: List[Union[str, TestDAta]]
#     b: Optional[str]


# @strict_attrs
# class MeetTest:
#     meet_data_list: List[MeetingStartedData]
#     asd: str


# @strict_dataclass
# class MeetTestDataClass:
#     meet_data_list: List[MeetingStartedDataClass]
#     asd: str


# def make_attr_obj():
#     MeetTest(
#         [
#             MeetingStartedData(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#             MeetingStartedData(
#                 "1", "2", 3, ["1", "2", TestDAta(11, "2")], "sdfsddas"
#             ),
#             MeetingStartedData(
#                 "1", "2", 3, ["1", "2", TestDAta(14, "2")], "sfsddas"
#             ),
#         ],
#         "32",
#     )


# def make_dataclass_obj():
#     MeetTestDataClass(
#         [
#             MeetingStartedDataClass(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#             MeetingStartedDataClass(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#             MeetingStartedDataClass(
#                 "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#             ),
#         ],
#         "32",
#     )


# attr_obj = MeetTest(
#     [
#         MeetingStartedData(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#         MeetingStartedData(
#             "1", "2", 3, ["1", "2", TestDAta(11, "2")], "sdfsddas"
#         ),
#         MeetingStartedData(
#             "1", "2", 3, ["1", "2", TestDAta(14, "2")], "sfsddas"
#         ),
#     ],
#     "32",
# )

# dataclass_obj = MeetTestDataClass(
#     [
#         MeetingStartedDataClass(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#         MeetingStartedDataClass(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#         MeetingStartedDataClass(
#             "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
#         ),
#     ],
#     "32",
# )


# def create_attr_dict():
#     asdict(attr_obj)


# def create_dataclass_dict():
#     dataclasses.asdict(dataclass_obj)


# time_1 = timeit.timeit(make_attr_obj, number=100000)
# time_2 = timeit.timeit(create_attr_dict, number=100000)
# time_3 = timeit.timeit(make_dataclass_obj, number=100000)
# time_4 = timeit.timeit(create_dataclass_dict, number=100000)


# print(f"Time taken to create attr objects is : {time_1}")
# print(f"Time taken to create dict of attr object is : {time_2}")
# print(f"Time taken to create dataclass objects is : {time_3}")
# print(f"Time taken to create dict of dataclass object is : {time_4}")

"""" --- --- ------- - -- -- -- - -- -- - -- -- - -- - -- -- - -- -- - - -- """


@strict_dataclass
class TestDAta:
    a: int
    b: str


@strict_dataclass
class MeetingStartedDataClass:
    attributes: Union[int, str]
    meeting_start_time: str
    a: int
    c: List[Union[str, TestDAta]]
    b: Optional[str]


@strict_dataclass
class MeetTestDataClass:
    meet_data_list: List[MeetingStartedDataClass]
    asd: str


@define
class MeetingStartedData:
    attributes: Union[int, str] = field(
        validator=validators.instance_of((int, str))
    )
    meeting_start_time: str = field(validator=validators.instance_of(str))
    a: int = field(validator=validators.instance_of(int))
    c: List[Union[str, TestDAta]] = field(
        validator=validators.deep_iterable(
            member_validator=validators.instance_of((str, TestDAta)),
            iterable_validator=validators.instance_of(list),
        )
    )
    b: Optional[str] = field(
        default=None, validator=validators.optional(validators.instance_of(str))
    )


@define
class MeetTest:
    meet_data_list: List[MeetingStartedData] = field(
        validator=validators.deep_iterable(
            member_validator=validators.instance_of(MeetingStartedData),
            iterable_validator=validators.instance_of(list),
        )
    )
    asd: str = field(validator=validators.instance_of(str))


@pydantic.dataclasses.dataclass
class PydanticDataClass:
    attributes: Union[int, str]
    meeting_start_time: str
    a: int
    c: List[Union[str, TestDAta]]
    b: Optional[str] = None


@pydantic.dataclasses.dataclass
class MeetTestPydanticDataClass:
    meet_data_list: List[PydanticDataClass]
    asd: str


def make_attr_obj():
    MeetTest(
        [
            MeetingStartedData(
                "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
            ),
            MeetingStartedData(
                "1", "2", 3, ["1", "2", TestDAta(11, "2")], "sdfsddas"
            ),
            MeetingStartedData(
                "1", "2", 3, ["1", "2", TestDAta(14, "2")], "sfsddas"
            ),
        ],
        "32",
    )


def make_dataclass_obj():
    MeetTestDataClass(
        [
            MeetingStartedDataClass(
                "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
            ),
            MeetingStartedDataClass(
                "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
            ),
            MeetingStartedDataClass(
                "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
            ),
        ],
        "32",
    )


def make_pydantic_obj():
    MeetTestPydanticDataClass(
        [
            PydanticDataClass(1, "1", 2, ["3", TestDAta(12, "2")], "sdfcdsc"),
            PydanticDataClass(1, "1", 2, ["3", TestDAta(12, "2")], "sedfcds"),
            PydanticDataClass(1, "1", 2, ["3", TestDAta(12, "2")], "sadassd"),
        ],
        "sda",
    )


attr_obj = MeetTest(
    [
        MeetingStartedData(
            "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
        ),
        MeetingStartedData(
            "1", "2", 3, ["1", "2", TestDAta(11, "2")], "sdfsddas"
        ),
        MeetingStartedData(
            "1", "2", 3, ["1", "2", TestDAta(14, "2")], "sfsddas"
        ),
    ],
    "32",
)

dataclass_obj = MeetTestDataClass(
    [
        MeetingStartedDataClass(
            "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
        ),
        MeetingStartedDataClass(
            "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
        ),
        MeetingStartedDataClass(
            "1", "2", 3, ["1", "2", TestDAta(12, "2")], "sdasdas"
        ),
    ],
    "32",
)

pydanctic_obj = MeetTestPydanticDataClass(
    [
        PydanticDataClass(1, "1", "2", ["3", TestDAta(12, "2")], "sdfcdsc"),
        PydanticDataClass(1, "1", "2", ["3", TestDAta(12, "2")], "sedfcds"),
        PydanticDataClass(1, "1", "2", ["3", TestDAta(12, "2")], "sadassd"),
    ],
    "1",
)
x = PydanticDataClass("1", "1", "2", ["3", TestDAta(12, "2")], "sdfcdsc")
# Ask if it is fine that pydanctic automatically converts values
x.a = ["s"]


def create_attr_dict():
    asdict(attr_obj)


def create_dataclass_dict():
    dataclasses.asdict(dataclass_obj)


def create_pydantic_dict():
    dataclasses.asdict(pydanctic_obj)


time_1 = timeit.timeit(make_attr_obj, number=100000)
time_2 = timeit.timeit(create_attr_dict, number=100000)
time_3 = timeit.timeit(make_dataclass_obj, number=100000)
time_4 = timeit.timeit(create_dataclass_dict, number=100000)
time_5 = timeit.timeit(make_pydantic_obj, number=100000)
time_6 = timeit.timeit(create_pydantic_dict, number=100000)


print(f"Time taken to create attr objects is : {time_1}")
print(f"Time taken to create dict of attr object is : {time_2}")
print(f"Time taken to create dataclass objects is : {time_3}")
print(f"Time taken to create dict of dataclass object is : {time_4}")
print(f"Time taken to create pydantic dataclass objects is : {time_5}")
print(f"Time taken to create dict of pydantic dataclass is : {time_6}")
