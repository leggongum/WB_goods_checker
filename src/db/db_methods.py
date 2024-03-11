from sqlalchemy import select

from db.db import session_factory
from db.models import Action


async def select_five_last_actions():
    async with session_factory() as session:
        q = select(Action).order_by(Action.id.desc()).limit(5)
        res = (await session.execute(q)).all()
        answer = []
        for action in res:
            answer.append({'id': action[0].id, 'user_id': action[0].user_id, 'articul': action[0].articul, 'timestamp': action[0].timestamp})
        return answer


async def insert_action(user_id: int, articul: int):
    async with session_factory() as session:
        session.add(Action(user_id=user_id, articul=articul))
        await session.commit()