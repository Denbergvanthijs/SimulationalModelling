using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlaneetBewegingKort : MonoBehaviour
{
    public int speed;

    void FixedUpdate()
    {
        transform.Rotate (new  Vector3(0, -10 * speed, 0) * Time.deltaTime); 
    }

    void LateUpdate(){
        transform.localPosition += transform.forward * Time.deltaTime * speed;
    }
}
