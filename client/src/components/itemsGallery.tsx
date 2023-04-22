import { useEffect, useState } from "react";
import { ItemDisplay, ItemData } from "./itemDisplay";
import { CardGroup } from "react-bootstrap";


export const ItemsGallery = () => {
    const [items, setItems] = useState<ItemData[]>(
       [],
      );
    
      useEffect(() => {
        fetch('/get-items').then((res) => 
          res.json().then((items) => {
            setItems(items)
          }));
      }, []);

    return (
        <div className="items-gallery">
            <CardGroup>
                {items.map((item, index) => 
                    <ItemDisplay 
                        name={item.name}
                        imageSource={item.imageSource}
                        price={item.price}
                    />
                )}
            </CardGroup>
        </div>
    );
  }