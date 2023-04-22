import React from "react";
import { Card } from "react-bootstrap";
import './itemDisplay.css'

export type ItemData = {
    name: string,
    price: number,
    imageSource: string
}

export const ItemDisplay = (itemData: ItemData) => {
    return (
        <div className="item-display">
            <Card>  
                <Card.Img variant="top" src={itemData.imageSource}/>
                <Card.Body>
                    <Card.Title>{itemData.name}</Card.Title>
                </Card.Body>
            </Card>
        </div>
    );
  }