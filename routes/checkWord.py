from fastapi import APIRouter, Body, HTTPException, Query

from models.check_word import CheckWordRequest, CheckWordResponse
from models.element import ElementRequest, ElementResponse
from modules.element_classifier import classify_element
from modules.semantic_similarity import MODEL_NAME, calculate_similarity


router = APIRouter(prefix="/api/check-word", tags=["check-word"])


def build_similarity_response(word1: str, word2: str) -> CheckWordResponse:
	clean_word1 = word1.strip()
	clean_word2 = word2.strip()

	if not clean_word1 or not clean_word2:
		raise HTTPException(status_code=400, detail="Both word1 and word2 are required")

	similarity_score, similarity_percent = calculate_similarity(clean_word1, clean_word2)
	return CheckWordResponse(
		word1=clean_word1,
		word2=clean_word2,
		similarity_score=similarity_score,
		similarity_percent=similarity_percent,
	)


@router.get("/similarity", response_model=CheckWordResponse)
def check_word_similarity_get(
	word1: str = Query(..., min_length=1, description="First word or phrase"),
	word2: str = Query(..., min_length=1, description="Second word or phrase"),
) -> CheckWordResponse:
	return build_similarity_response(word1, word2)


@router.post("/similarity", response_model=CheckWordResponse)
def check_word_similarity(
	payload: CheckWordRequest | None = Body(default=None),
	word1: str | None = Query(default=None, min_length=1, description="First word or phrase"),
	word2: str | None = Query(default=None, min_length=1, description="Second word or phrase"),
) -> CheckWordResponse:
	if payload is not None:
		return build_similarity_response(payload.word1, payload.word2)

	if word1 is not None and word2 is not None:
		return build_similarity_response(word1, word2)

	raise HTTPException(
		status_code=400,
		detail="Send word1 and word2 in JSON body or query parameters",
	)


@router.post("/element", response_model=ElementResponse)
def check_word_element(payload: ElementRequest) -> ElementResponse:
	clean_word = payload.word.strip()
	if not clean_word:
		raise HTTPException(status_code=400, detail="word is required")

	return ElementResponse(element=classify_element(clean_word))
