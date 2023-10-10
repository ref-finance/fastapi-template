# @Time : 10/7/23 1:56 PM
# @Author : HanyuLiu/Rainman
# @Email : rainman@ref.finance
# @File : routes.py
from fastapi import APIRouter, HTTPException
from starlette.requests import Request

from core.utils.base_util import get_limiter
import logging
from apps.test_app.models import TestTable

logger = logging.getLogger(__name__)
limiter = get_limiter()
router = APIRouter(prefix="/api/test")

@router.get('/cool', tags=['test'])
@limiter.limit('100/minute')
async def test(request: Request):
    all_data = await TestTable.all()
    return all_data

