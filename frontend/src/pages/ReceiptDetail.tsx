import React from 'react'
import { useParams } from 'react-router-dom'

export default function ReceiptDetail() {
  const { id } = useParams<{ id: string }>()
  return <h1>Receipt Detail: {id}</h1>
}