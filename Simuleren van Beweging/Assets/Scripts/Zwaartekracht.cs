using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Zwaartekracht : MonoBehaviour
{
    public Vector3 Force;
    public Vector3 Acceleration;
    public Vector3 Velocity;
    public int mass;

    void Start()
    {
    }

    void FixedUpdate()
    {
        Acceleration = Force / mass;
        Velocity += Acceleration * Time.deltaTime;
        transform.position += Velocity * Time.deltaTime;
    }
}
