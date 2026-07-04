from pyrogram import filters
from pyrogram.types import Message


def group_only(_, __, message: Message):
    return message.chat.type in ("group", "supergroup")


def admins_only(_, __, message: Message):
    member = message.chat.get_member(message.from_user.id)
    return member.status in ("administrator", "creator")


group_filter = filters.create(group_only)
admin_filter = filters.create(admins_only)