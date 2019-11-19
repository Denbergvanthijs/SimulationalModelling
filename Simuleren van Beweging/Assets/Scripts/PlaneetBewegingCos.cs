using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;


public class PlaneetBewegingCos : MonoBehaviour
{
    public int speed;
    public int steps;
    private float hoek;
    private int i;


    void FixedUpdate()
    {
        hoek = (float)(2 * Math.PI * i / steps);
        i++;
        transform.localPosition += new Vector3((float)Math.Cos(hoek), 0, (float)Math.Sin(hoek)) * speed * Time.deltaTime;
    }
}

