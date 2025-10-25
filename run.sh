#!/bin/bash
echo "🚀 Starting PDF Chat..."
uvicorn app.main:app --reload
