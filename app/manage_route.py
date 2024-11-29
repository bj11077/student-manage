from fastapi import APIRouter
from typing import List
from manage_model import ResponseForm,Student
import manage_service as service 
import logging



status_router = APIRouter(prefix='/api/manage')

@status_router.on_event('startup')
async def router_startup():
    logging.info("Router startup: initializing resources...")

@status_router.get('')
async def get_status() -> ResponseForm:
    return ResponseForm(data=service.get_student_list())

@status_router.post('')
async def save_status(server_status:Student) -> ResponseForm:
    return ResponseForm(data=service.save_student_list())

@status_router.put('')
async def update_status(server_status:Student) -> ResponseForm:
    return ResponseForm(data=service.save_student_list())

@status_router.delete('/{manage_id}')
async def delete_status(manage_id:str) -> ResponseForm:
    return ResponseForm(data=service.delete_student(manage_id))