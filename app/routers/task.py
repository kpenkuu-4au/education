from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from app.backend.db_depends import get_db
from typing import Annotated
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task)).all()
    return tasks


@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )
    else:
        return task


@router.post('/create')
async def create_task(
                                db: Annotated[Session, Depends(get_db)],
                                user_id: int,
                                new_task: CreateTask
                                ):
    found_user = db.scalar(select(User).where(User.id == user_id))
    tasks = db.scalars(select(Task)).all()
    if found_user is not None and tasks == []:
        db.execute(insert(Task).values(
            id=1,
            title=new_task.title,
            content=new_task.content,
            priority=new_task.priority,
            completed=False,
            user_id=found_user.id,
            slug=slugify(new_task.title)
        )
        )
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    elif found_user is not None:
        db.execute(insert(Task).values(
            id=tasks[-1].id + 1,
            title=new_task.title,
            content=new_task.content,
            priority=new_task.priority,
            completed=False,
            user_id=found_user.id,
            slug=slugify(new_task.title)
        )
        )
        db.commit()
        return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='User was not found'
        )


@router.put('/update')
async def update_task(
                                    db: Annotated[Session, Depends(get_db)],
                                    task_id: int,
                                    upd_task: UpdateTask
                                ):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
                                        status_code=status.HTTP_404_NOT_FOUND,
                                        detail='Task was not found'
                                    )
    else:
        db.execute(update(Task).where(Task.id == task_id).values(
                                                                                firstname=upd_task.firstname,
                                                                                lastname=upd_task.lastname,
                                                                                age=upd_task.age
                                                                                )
                        )
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task update is successful!'}


@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)], task_id: int):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is None:
        raise HTTPException(
                                        status_code=status.HTTP_404_NOT_FOUND,
                                        detail='Task was not found'
                                    )
    else:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK, 'transaction': 'Task delete is successful!'}
